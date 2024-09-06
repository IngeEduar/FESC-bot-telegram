CREATE TABLE menu (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE
);


CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    response TEXT,
);

CREATE TABLE question_options (
    question_id INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    option_id INTEGER REFERENCES questions(id) ON DELETE CASCADE,
    PRIMARY KEY (question_id, option_id)
);
