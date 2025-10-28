CREATE TABLE category (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE course (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    study_time INTEGER NOT NULL,
    cost NUMERIC(10, 2) NOT NULL,
    format VARCHAR(100) NOT NULL,
    education_type VARCHAR(100) NOT NULL,
    issued_document VARCHAR(255) NOT NULL,
    category_id BIGINT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_course_category
        FOREIGN KEY (category_id)
        REFERENCES category (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE "user" (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    password TEXT NOT NULL
);

CREATE TABLE user_course (
    user_id BIGINT NOT NULL,
    course_id BIGINT NOT NULL,
    CONSTRAINT pk_user_course PRIMARY KEY (user_id, course_id),
    CONSTRAINT fk_user_course_user
        FOREIGN KEY (user_id)
        REFERENCES "user" (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_user_course_course
        FOREIGN KEY (course_id)
        REFERENCES course (id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
