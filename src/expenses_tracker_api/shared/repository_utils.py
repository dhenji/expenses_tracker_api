from collections.abc import Sequence
from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from expenses_tracker_api.shared.exceptions_mapper import (
    map_query_error,
    map_write_error,
)


def save_entity[T](session: Session, entity: T) -> T:
    try:
        session.add(entity)
        session.flush()

        return entity
    except SQLAlchemyError as e:
        raise map_write_error(e) from e


def get_all_entities[T](session: Session, model_class: type[T]) -> Sequence[T]:
    try:
        stmt: Select[tuple[T]] = select(model_class)
        return session.scalars(stmt).all()
    except SQLAlchemyError as e:
        raise map_query_error(e) from e


def get_entity[T](session: Session, model_class: type[T], *, id: Any) -> T | None:
    try:
        return session.get(model_class, id)
    except SQLAlchemyError as e:
        raise map_query_error(e) from e


def get_entity_by[T](session: Session, model_class: type[T], **kwargs: Any) -> T | None:
    if not kwargs:
        raise ValueError("Atleast one filter is required.")

    try:
        stmt: Select[tuple[T]] = select(model_class).where(
            *[getattr(model_class, k) == v for k, v in kwargs.items()]
        )
        return session.scalars(stmt).one_or_none()
    except SQLAlchemyError as e:
        raise map_query_error(e) from e


def delete_entity[T](session: Session, entity: T) -> None:
    try:
        session.delete(entity)
    except SQLAlchemyError as e:
        raise map_write_error(e) from e
