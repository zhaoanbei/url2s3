# url2s3

目标是提供一个url, 通过lambda下载并上传到s3。需要lambda 有ECR read以及S3 write权限。如果在国内/tmp空间不足，可以挂载EFS，lambda需要对应EFS write权限，app.py需要修改本地路径位置到efs的挂载点。

在海外lambda可以有public url, 国内用sdk调用（python_invoke.ipynb）或者加api gateway。

首先在aws ecr上创建一个镜像仓库，然后docker build 并push镜像

在创建lambda时选择镜像来源，选择latest镜像。
test事件格式：{
  "url": "xx",
  "bucket": "xx",
  "prefix": "xx"
}

然后打开python_invoke.ipynb可以调用。