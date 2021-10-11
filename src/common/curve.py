from pyjava.api.mlsql import RayContext,PythonContext
from pyecharts import options as opts
from pyecharts.charts import Line
import os

context:PythonContext = context

ray_context = RayContext.connect(globals(),None)
df = ray_context.to_pandas()
df = df.sort_values(context.conf["x"])

c3=(
   Line()
.add_xaxis(list(df[context.conf["x"]]))
.add_yaxis(context.conf["yName"], list(df[context.conf["y"]]))    
.set_global_opts(title_opts=opts.TitleOpts(title=context.conf["title"]))
.render("line_dnu.html")
)

html = ""
with open("line_dnu.html") as file:
   html = "\n".join(file.readlines())

os.remove("line_dnu.html")
context.build_result([{"content":html,"mime":"html"}])