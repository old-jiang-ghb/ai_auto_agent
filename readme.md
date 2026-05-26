## 技术栈

- 后端：Python

## 项目结构

```
ai_auto_agent/
├── core/       		 # 核心配置（数据库、异常、middleware）
├── dubbo_module/        # dubbo接入模块
├── prompts/ 			 # 提示词 
├── service/ 			 # service层
├── utils/ 				 # 工具类
├── xianyu_auto_agent/ 	 # 闲鱼24小时客服自动化agent
   └── xianyu_main.py    # 闲鱼客服项目入口
```

## 快速启动

### 1. 克隆项目

bash

运行

```
git clone https://github.com/old-jiang-ghb/ai_auto_agent.git
cd ai_auto_agent
```

### 2. 安装依赖

bash

运行

```
pip install -r requirements.txt
```

### 3. 启动服务

bash

运行

```
python xianyu_auto_agent/xianyu_main.py
```

## 使用场景

- 闲鱼24h自动客服，可以使用项目中默认的客服agent，也可以外接rag接口进行答复

## 关于作者

GitHub：old-jiang-ghb