import sys
import platform
import datetime

print("✅ Python 환경 점검 결과")
print("---------------------------")
print(f"Python 버전      : {platform.python_version()}")
print(f"실행 위치        : {sys.executable}")
print(f"운영체제         : {platform.system()} {platform.release()}")
print(f"현재 시각        : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("---------------------------")
print("🎉 환경이 정상적으로 작동하고 있습니다!")
