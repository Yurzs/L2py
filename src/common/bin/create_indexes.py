import asyncio

import common.modelsx  # noqa
from src.common.common.document import Document


async def main():
    for model in Document.__subclasses__():
        if hasattr(model, "create_index"):
            await model.create_index()


if __name__ == "__main__":
    asyncio.run(main())
