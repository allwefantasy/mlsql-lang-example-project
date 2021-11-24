# MLSQL Lang example project

This is a mlsql-lang example project.

## Installation Of MLSQL Lang IDE


1. Download [Visual Studio Code](https://code.visualstudio.com/)
2. Download MLSQL Lang VSCode plugin
    * [Winwdows](http://download.mlsql.tech/mlsql-win-0.0.6.vsix)
    * [Mac](http://download.mlsql.tech/mlsql-mac-0.0.6.vsix)
    * [Linux](http://download.mlsql.tech/mlsql-linux-0.0.6.vsix)



After installation of `Visual Studio Code` , switch to  `Extensions` tab, click `...` on right side of search bar, find the item `Install from VSIX...`, choose the VSCode plugin we had already downloaded in preview step and intall it.

![](http://store.mlsql.tech/upload_images/fcc2091a-db9a-4248-96d9-680bc32a7594.png)


Notice that for now we only support Ligt theme in vscode.
Select Code > Preferences > Color Theme :

![](http://store.mlsql.tech/upload_images/011d67b6-0a98-445f-9e59-8c940462718e.png)


In command palette popup，select the light color:

![](http://store.mlsql.tech/upload_images/96b0e81f-1856-4c8a-9bb6-84d8180e7968.png)

## Download this project

Click `Clone or download` and select  `Download ZIP`, then you get the package of this project. Unzip it in you desktop.

![](http://store.mlsql.tech/upload_images/f67b7e1d-968d-4a2f-af36-3c0e14730d83.png)


## Open this project in vscode

Select File > Open...  and choose the location where we unzip this project.

## Tutorial

1. `./src/try_mlsql` is a good start point for you to learn MLSQL.
2. `./src/a_tour_of_mlsql` you can learn full picture of MLSQL Lang.
3. `./src/examples/examples` there are many mlsql code snippets in this notebook.
4. `./analysis/example/cifar10/ResizeImage` teach you how to processing image distributly.
5. `./analysis/example/cifar10/DistributeTFTrainning` teach you how to train DL by tensorflow distributly.

## Python Script Support

`Ray` is a build-in plugin in MLSQL which can execute Python script. 

The power part is that you can 
access the data in target table in Python and pass the result processed back as a new table.

Some limitation for now:

1. The schema of python output should be specified mannually.

```shell
!python conf "schema=st(field(a,long))";
```

The basic python dependencies:

```
pyarrow==4.0.1
ray[default]
aiohttp==3.7.4
pandas>=1.0.5; python_version < '3.7'
pandas>=1.2.0; python_version >= '3.7'
requests
matplotlib~=3.3.4
uuid~=1.30
pyjava
```

Suppose you can have created virtual python enviroment called `ray1.8.0` (this will used by example in this project by default). 

```
conda create  --name ray1.8.0 python=3.6
```
and make sure you have the aforementioned dependencies are also installed.


