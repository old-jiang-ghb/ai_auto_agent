import sys
import json
import logging
from loguru import logger
from logging_loki import LokiHandler

# ==================== 【企业配置】 ====================
LOKI_URL = "http://192.168.236.102:3100/loki/api/v1/push"
SERVICE = "ai-auto-agent"
ENV = "prod"
VERSION = "1.0.0"

# ==================== 清空原有日志输出 ====================
logger.remove()

# ==================== 1. 控制台输出（美观） ====================
logger.add(
    sys.stdout,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "trace_id=<cyan>{extra[trace_id]}</cyan> | "
        "user_id=<blue>{extra[user_id]}</blue> | "
        "{message}"
    ),
    enqueue=True,
    level="INFO"
)

# ==================== 2. 【核心】结构化日志格式化器 ====================
# class StructuredLokiFormatter(logging.Formatter):
#     """
#     企业级结构化日志格式化器
#     输出 JSON 格式，方便 Grafana 按字段检索
#     """
#     def format(self, record):
#         # 基础字段
#         log_data = {
#             "timestamp": record.created,
#             "level": record.levelname,
#             "message": record.getMessage(),
#             "service": SERVICE,
#             "env": ENV,
#             "version": VERSION,
#         }
#
#         # 自定义上下文字段（从 Loguru 的 extra 中获取）
#         if hasattr(record, "trace_id"):
#             log_data["trace_id"] = record.trace_id
#         if hasattr(record, "user_id"):
#             log_data["user_id"] = record.user_id
#         if hasattr(record, "session_id"):
#             log_data["session_id"] = record.session_id
#         if hasattr(record, "module"):
#             log_data["module"] = record.module
#
#         # 异常堆栈信息
#         if record.exc_info:
#             log_data["exception"] = self.formatException(record.exc_info)
#
#         # 返回 JSON 字符串（Loki 可以直接解析）
#         return json.dumps(log_data, ensure_ascii=False)
#
# # ==================== 3. Loki Handler 配置 ====================
# loki_tags = {
#     "service": SERVICE,
#     "env": ENV,
#     "version": VERSION
# }
#
# loki_handler = LokiHandler(
#     url=LOKI_URL,
#     tags=loki_tags,
#     level=logging.INFO,
#     timeout=10,
#     async_=True  # 异步推送，不阻塞主线程/流式输出
# )
#
# # 给 LokiHandler 绑定我们自己的格式化器
# loki_handler.setFormatter(StructuredLokiFormatter())
#
# # ==================== 4. 把 Loki 接入 Loguru ====================
# logger.add(
#     loki_handler,
#     enqueue=True,    # 异步队列，保证不阻塞
#     backtrace=True,
#     diagnose=False
# )
#
# # ==================== 使用示例 ====================
# if __name__ == "__main__":
#     logger.bind(
#         trace_id="trace_123456",
#         user_id=1001,
#         session_id=2001,
#         module="chat_stream"
#     ).info("AI客服流式对话开始")
#
#     try:
#         1 / 0
#     except Exception:
#         logger.bind(trace_id="trace_123456").exception("AI服务异常")