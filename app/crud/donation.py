from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):
    async def get_by_user_donations(
        self,
        donation: Donation,
        user: User,
        session: AsyncSession,
    ) -> List:
        return (
            (await session.execute(select(donation).where(donation.user_id == user.id)))
            .scalars()
            .all()
        )


donation_crud = CRUDDonation(Donation)
