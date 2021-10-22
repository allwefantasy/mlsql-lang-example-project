from typing import List
from pyjava.storage import streaming_tar
import ray
import os
import numpy as np
import tempfile
from pyjava.serializers import ArrowStreamSerializer
from xgboost_ray import RayDMatrix, RayParams, train
from pyjava.api.mlsql import PythonContext, RayContext
from pyjava import rayfix

context:PythonContext = context
conf = context.conf
ray_context = RayContext.connect(globals(),conf["rayAddress"])

# if we use modin `ModuleNotFoundError: No module named 'modin.distributed'` will throws
# data_refs = ray_context.data_servers()

# def fetch_data_from_single_data_server(data_server):
#     out_ser = ArrowStreamSerializer()
#     import pyarrow as pa
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.connect((data_server.host, data_server.port))
#         buffer_size = int(os.environ.get("BUFFER_SIZE", 65536))
#         infile = os.fdopen(os.dup(sock.fileno()), "rb", buffer_size)
#         result = out_ser.load_stream(infile)
#         return pa.Table.from_batches(result)        

# @ray.remote
# @rayfix.last
# def fetchData(data_ref:str):
#      table = fetch_data_from_single_data_server(data_ref)
#      return table

# refs = [fetchData.remote(data_ref) for data_ref in data_refs]
# tables = [ray.get(ref) for ref in refs]

# # distributed pandas
# dpd = ray.data.from_arrow(tables).to_modin()


@ray.remote
@rayfix.last
def rtrain(data_refs:List[str]):
    rows = [row for row in RayContext.collect_from(data_refs) ]
    train_x = np.array([np.array(row["features"]) for row in rows])
    train_y = np.array([row["label"] for row in rows])
    train_set = RayDMatrix(train_x, train_y) 

    print(train_x)
    print(train_y)

    evals_result = {}

    bst = train(
        {
            "objective": "binary:logistic",
            "eval_metric": ["logloss", "error"],
        },
        train_set,
        evals_result=evals_result,
        evals=[(train_set, "train")],
        verbose_eval=False,
        ray_params=RayParams(
            num_actors=2,  # Number of remote actors
            cpus_per_actor=1))

    base_dir = os.path.join(tempfile.gettempdir(),"xgboost")
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    bst.save_model(os.path.join(base_dir,"model.xgb"))
    items = streaming_tar.build_rows_from_file(base_dir)
    return [item for item in items]

items = ray.get(rtrain.remote(ray_context.data_servers()))
context.build_result(items)


