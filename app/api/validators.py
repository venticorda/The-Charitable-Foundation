from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_charity_project_name_duplicate(
    project_name: str,
    session: AsyncSession,
):
    """Проверяет, существует ли проект с таким же именем."""
    project_id = await charity_project_crud.get_charity_project_by_name(
        project_name, session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Проект с таким именем уже существует!",
        )


def check_charity_project_invested_amount(
        project: CharityProject, new_amount: int):
    """Проверяет, нельзя ли установить сумму, ниже уже вложенной."""
    if project.invested_amount > new_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Нельзя установить сумму, ниже уже вложенной!",
        )


async def check_charity_project_exists(
    project_id: int,
    session: AsyncSession,
):
    """Проверяет, существует ли проект с заданным идентификатором."""
    project = await charity_project_crud.get_charity_project_by_id(
        project_id, session)
    if project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Проект не найден!"
        )
    return project


def check_charity_project_not_empty(charity_project: CharityProject):
    """Проверяет, нет ли в проекте вложений."""
    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="В проект были внесены средства, не подлежит удалению!",
        )


def check_charity_project_is_closed(charity_project: CharityProject):
    """Проверяет, закрыт ли проект."""
    if charity_project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Закрытый проект нельзя редактировать!",
        )
