
import sys

# 上级目录文件
# sys.path.append('../')
# import mtest

# 同级子目录
# sys.path.append('/home/steven/Test/python_package_dir/mypackage/sub2')
sys.path.append('../sub2')
import test2
#
print(sys.path)


def test1():
	print("test1")

test1()
