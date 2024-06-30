from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get_charity_project_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        return (
            (
                await session.execute(
                    select(CharityProject.id).where(CharityProject.name == project_name)
                )
            )
            .scalars()
            .first()
        )

    async def get_charity_project_by_id(
        self,
        project_id: int,
        session: AsyncSession,
    ) -> Optional[CharityProject]:
        return (
            (
                await session.execute(
                    select(CharityProject).where(CharityProject.id == project_id)
                )
            )
            .scalars()
            .first()
        )

    async def get_projects_by_completion_rate(
        self, session: AsyncSession
    ) -> Optional[CharityProject]:
        return (
            (
                await session.execute(
                    select(CharityProject)
                    .where(CharityProject.fully_invested == 1)
                    .order_by(
                        func.extract(
                            "epoch",
                            CharityProject.close_date - CharityProject.create_date,
                        ).asc()
                    )
                )
            )
            .scalars()
            .all()
        )


charity_project_crud = CRUDCharityProject(CharityProject)
