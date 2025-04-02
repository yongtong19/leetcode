CXX = g++
CXXFLAGS = -std=c++17 -Wall -g
OUT_DIR = out
INCLUDES = -I./include

# 创建输出目录
$(shell mkdir -p $(OUT_DIR))

# 主规则
%: %.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) $< -o $(OUT_DIR)/$@
	@echo "=== Running $(OUT_DIR)/$@ ==="
	@./$(OUT_DIR)/$@
	@echo "=== Finished ==="

# 只编译不运行
%.build: %.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) $< -o $(OUT_DIR)/$*

clean:
	rm -rf $(OUT_DIR)