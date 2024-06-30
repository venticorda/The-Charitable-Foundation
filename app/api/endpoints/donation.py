from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import CharityProject, Donation, User
from app.schemas.donation import DonationBase, DonationCreate, DonationDB
from app.services.investment import invest_process

router = APIRouter()


@router.post(
    "/",
    response_model=DonationCreate,
    response_model_exclude_none=True,
)
async def create_donation(
    donation: DonationBase,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Создание пожертвования."""
    new_donation = await donation_crud.create(
        obj_in=donation, session=session, user=user
    )
    await invest_process(new_donation, CharityProject, session)
    return new_donation


@router.get(
    "/",
    response_model=List[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)):
    """Получение всех пожертвований."""
    all_donations = await donation_crud.get_multi(session=session)
    return all_donations


@router.get(
    "/my",
    response_model=List[DonationCreate],
    response_model_exclude={"user_id"},
)
async def get_user_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """Получение пожертвований пользователя."""
    donations = await donation_crud.get_by_user_donations(
        Donation, session=session, user=user
    )
    return donations
