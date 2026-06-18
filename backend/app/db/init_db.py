"""
数据库初始化模块
"""
import logging

from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


async def init_db(db: AsyncSession) -> None:
    """
    初始化数据库。

    生产部署不自动创建演示账户或演示数据；管理员账户应通过受控的数据库
    或运维流程创建。
    """
    logger.info("开始初始化数据库...")
    logger.info("跳过演示账户和演示数据创建")

    # 初始化系统模板和规则
    try:
        from app.services.init_templates import init_templates_and_rules
        await init_templates_and_rules(db)
    except Exception as e:
        logger.warning(f"初始化模板和规则跳过: {e}")

    logger.info("数据库初始化完成")
