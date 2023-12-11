import time
from llama_cpp import Llama

# 开始计时 - 模型加载
model_load_start = time.time()
# 创建 Llama 模型实例
llm = Llama(model_path="Mistral-7B-Instruct-v01-GGUF/mistral-7b-instruct-v0.1.Q4_K_M.gguf")
# 模型加载完成
model_load_end = time.time()

# 计算模型加载时间
model_load_time = model_load_end - model_load_start
print(f"模型加载时间：{model_load_time} 秒")

# 进行多次推理
num_iterations = 5  # 可以根据需要调整循环次数
for i in range(num_iterations):
    # 开始计时 - 推理
    inference_start = time.time()

    # 调用模型生成文本
    output = llm(
        "Q: Name the planets in the solar system? A: ",
        max_tokens=32,
        stop=["Q:", "\n"],
        echo=True
    )

    # 结束计时 - 推理
    inference_end = time.time()

    # 计算并打印每次推理所需时间
    elapsed_time = inference_end - inference_start
    print(f"第 {i + 1} 次推理所需时间：{elapsed_time} 秒")

    # 打印生成的文本
    print(output['choices'][0]['text'])
