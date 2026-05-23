import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

STEP_CAD_DIR = "D:\\0Learn\\myself\\vibe-coding\\step_cad_harness\\step_to_process\\only_viewer"

async def get_mcp_tools_async():
    client = MultiServerMCPClient(
        {
            "step-cad-assembly-tools": {
                "transport": "stdio",
                "command": "node",
                "args": ["mcp-server.js"],
                "cwd": STEP_CAD_DIR,
                "env": {
                    "STEP_CAD_PROJECT_ROOT": f"{STEP_CAD_DIR}/project-data",
                },
                "encoding": "utf-8",
            }
        }
    )
    return await client.get_tools()

def get_mcp_tools():
    return asyncio.run(get_mcp_tools_async())


if __name__ == "__main__":
    tools = get_mcp_tools()
    print(len(tools))
    print([t.name for t in tools])
    tool_name = "cad_render_part_multiview"
    # 根据tool_name找到对应的工具
    tool = next((t for t in tools if t.name == tool_name), None)
    if not tool:
        print(f"Tool '{tool_name}' not found.")
        exit(1)
    # 根据工具定义构造输入参数
        # 构建输入参数
    print(f"Testing tool: {tool.name}")
    input_dict = {
        "project_id": "7a3178cd-a0fe-400a-b782-4718448ae92f",
        "part_id": "node-4",
        "size": 256,
    }
    result = asyncio.run(tool.arun(tool_input = input_dict))
    print(type(result))   # <class 'list'>
    print(len(result))     # 打印前两个元素看看结构
    print(result)      # 打印第一个元素看看结构
    # # 将result 文本解析为 JSON 对象并保存到文件
    # import json

    # # 假设 result['text'] 是 JSON 字符串
    # json_str = result[0]['text']

    # # 将 JSON 字符串解析成 Python 对象
    # data = json.loads(json_str)

    # # 写入文件，输出标准 JSON 格式
    # with open("contact_candidates.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)
