"""seed default expense categories

Revision ID: ed4ac8f928f4
Revises: 9b04f42c35dd
Create Date: 2026-08-22 10:51:31.062898

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ed4ac8f928f4"
down_revision: Union[str, Sequence[str], None] = "9b04f42c35dd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


SEED_CATEGORIES_SQL = """
INSERT INTO public.categories (name, description)
VALUES
  ('Housing', 'Rent, mortgage, property taxes, and home maintenance'),
  ('Utilities', 'Electricity, water, gas, internet, and phone bills'),
  ('Food and Drinks', 'Groceries, dining out, and beverages'),
  ('Transportation', 'Fuel, public transit, parking, and vehicle maintenance'),
  ('Healthcare', 'Medical visits, insurance, prescriptions, and wellness'),
  ('Shopping', 'Clothing, electronics, and general merchandise'),
  ('Entertainment', 'Movies, games, streaming services, and hobbies'),
  ('Travel', 'Flights, accommodation, and trip expenses'),
  ('Education', 'Tuition, courses, books, and learning materials'),
  ('Work and Business', 'Office supplies, professional services, and business expenses'),
  ('Personal Care', 'Grooming, skincare, and self-care products'),
  ('Family and Kids', 'Childcare, school supplies, and family activities'),
  ('Financial', 'Bank fees, investments, and interest payments'),
  ('Gift and Donation', 'Gifts for others and charitable contributions'),
  ('Miscellaneous', 'Other expenses that do not fit any other category')
ON CONFLICT (name) DO NOTHING;
"""

CATEGORY_NAMES = [
    "Housing",
    "Utilities",
    "Food and Drinks",
    "Transportation",
    "Healthcare",
    "Shopping",
    "Entertainment",
    "Travel",
    "Education",
    "Work and Business",
    "Personal Care",
    "Family and Kids",
    "Financial",
    "Gift and Donation",
    "Miscellaneous",
]


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(SEED_CATEGORIES_SQL)


def downgrade() -> None:
    """Downgrade schema."""
    op.get_bind().execute(
        sa.text("DELETE FROM public.categories WHERE name IN :names").bindparams(
            sa.bindparam("names", expanding=True)
        ),
        {"names": CATEGORY_NAMES},
    )
