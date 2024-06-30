from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_charity_project_exists,
    check_charity_project_invested_amount,
    check_charity_project_is_closed,
    check_charity_project_name_duplicate,
    check_charity_project_not_empty,
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.models import Donation
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate,
)
from app.services.investment import invest_process

router = APIRouter()


@router.post(
    "/",
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Создание проекта. Только для суперпользователя.
    """
    await check_charity_project_name_duplicate(charity_project.name, session)
    await charity_project_crud.get_charity_project_by_name(
        charity_project.name, session
    )
    new_project = await charity_project_crud.create(charity_project, session)
    await invest_process(new_project, Donation, session)
    return new_project


@router.get(
    "/",
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(session: AsyncSession = Depends(get_async_session)):
    """
    Получение всех проектов.
    """
    projects = await charity_project_crud.get_multi(session=session)
    return projects


@router.patch(
    "/{project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Обновление проекта. Только для суперпользователя."""
    project = await check_charity_project_exists(project_id, session)
    check_charity_project_is_closed(project)
    if obj_in.name:
        await check_charity_project_name_duplicate(obj_in.name, session)
    if obj_in.full_amount is not None:
        check_charity_project_invested_amount(project, obj_in.full_amount)
    update_project = await charity_project_crud.update(project, obj_in, session)
    return update_project


@router.delete(
    "/{project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Удаление проекта. Только для суперпользователя."""
    project = await check_charity_project_exists(project_id, session)
    check_charity_project_not_empty(project)
    charity_project = await charity_project_crud.remove(project, session)
    return charity_project
