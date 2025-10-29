import asyncio
from faker import Faker
from random import randint, choice, uniform
from decimal import Decimal
from datetime import datetime, timedelta

from sqlalchemy import select

from app.core.db import async_session
from app.models.category import Category
from app.models.course import Course
from app.models.user import User


fake = Faker("en_US")

NUM_CATEGORIES = 5
NUM_COURSES = 15
NUM_USERS = 20


def random_price() -> Decimal:
    value = round(uniform(100, 5000), 2)
    return Decimal(str(value))


def random_timestamp() -> datetime:
    days_ago = randint(0, 30)
    return datetime.utcnow() - timedelta(days=days_ago)


async def seed_categories(db):
    result = await db.execute(select(Category))
    existing = result.scalars().all()
    if existing:
        return existing

    categories = []
    for _ in range(NUM_CATEGORIES):
        cat = Category(
            name=fake.job(),
        )
        db.add(cat)
        categories.append(cat)

    await db.commit()

    for c in categories:
        await db.refresh(c)

    return categories


async def seed_courses(db, categories):
    result = await db.execute(select(Course))
    existing = result.scalars().all()
    if existing:
        return existing

    courses = []
    for _ in range(NUM_COURSES):
        category = choice(categories)

        created_at = random_timestamp()
        updated_at = created_at + timedelta(days=randint(0, 5))

        course = Course(
            title=fake.sentence(nb_words=4).rstrip("."),
            description=fake.paragraph(nb_sentences=3),
            study_time=randint(10, 200),
            cost=random_price(),
            format=choice(["online", "offline", "hybrid"]),
            education_type=choice(["professional", "higher", "course", "seminar"]),
            issued_document=choice(
                ["сертификат", "удостоверение", "диплом", "без документа"]
            ),
            category_id=category.id,
            created_at=created_at,
            updated_at=updated_at,
        )

        db.add(course)
        courses.append(course)

    await db.commit()

    for c in courses:
        await db.refresh(c)

    return courses


async def seed_users(db):
    result = await db.execute(select(User))
    existing = result.scalars().all()
    if existing:
        return existing

    users = []
    for _ in range(NUM_USERS):
        first = fake.first_name()
        last = fake.last_name()

        raw_phone = fake.phone_number()
        safe_phone = raw_phone[:20]  # обрежем до 20 символов

        user = User(
            first_name=first,
            middle_name=fake.first_name() if randint(0, 1) else None,
            last_name=last,
            email=fake.unique.email(),
            phone_number=safe_phone,
            password="hashed_password_example",
        )

        db.add(user)
        users.append(user)

    await db.commit()

    for u in users:
        await db.refresh(u)

    return users


async def main():
    async with async_session() as db:
        categories = await seed_categories(db)
        await seed_courses(db, categories)
        await seed_users(db)

    print("[seed] fake data inserted successfully")


if __name__ == "__main__":
    asyncio.run(main())
