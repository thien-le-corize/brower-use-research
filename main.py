import asyncio
from dotenv import load_dotenv
from browser_use import Agent, Browser
from browser_use.llm import ChatBrowserUse

load_dotenv()

async def run_login_test(username: str, password: str, expected: str):
    browser = Browser(headless=False)
    llm = ChatBrowserUse()

  
  

    task = "\n".join(f"Step {i+1}: {s}" for i, s in enumerate(steps))

    agent = Agent(task=task, llm=llm, browser=browser)
    result = await agent.run()

    result_text = str(result.output if hasattr(result, 'output') else result)

    return {
        "username": username,
        "password": password,
        "expected": expected,
        "result": result_text.strip()
    }

async def main():
    # test case login
    test_cases = [
        {"username": "admin", "password": "admin123", "expected": "THÀNH CÔNG"},
        {"username": "admin", "password": "wrongpass", "expected": "THẤT BẠI"},
    ]

    results = []

    for case in test_cases:
        print(f"\n🚀 RUNNING TEST CASE: {case['username']} ({case['expected']})")
        res = await run_login_test(case["username"], case["password"], case["expected"])
        results.append(res)

    # bảng kết quả
    print("\n" + "="*100)
    print("📌 KẾT QUẢ TEST ĐĂNG NHẬP")
    print("="*100)
    print(f"{'STT':<4} {'Username':<12} {'Password':<15} {'Kỳ vọng':<12} {'Thực tế':<10} {'Message'}")
    print("-"*100)

    for i, row in enumerate(results, 1):
        actual = "THÀNH CÔNG" if "THÀNH CÔNG" in row["result"].upper() else "THẤT BẠI"
        msg = row["result"].replace("\n", " ").strip()[:80] + "..."
        print(f"{i:<4} {row['username']:<12} {row['password']:<15} {row['expected']:<12} {actual:<10} {msg}")

    print("="*100)


if __name__ == "__main__":
    asyncio.run(main())
