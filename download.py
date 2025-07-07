from modelscope import snapshot_download
model_dir = snapshot_download('Qwen/Qwen2.5-VL-3B-Instruct',
                              local_dir='/home/fengjingxi/fengjingxi_data1/llm/model')
print(f"模型已下载到: {model_dir}")