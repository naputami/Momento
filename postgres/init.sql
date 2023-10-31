CREATE extension IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v4();

CREATE TABLE users(
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    username VARCHAR(124) NOT NULL,
    name VARCHAR(124) NOT NULL,
    email VARCHAR(124) NOT NULL UNIQUE,
    password_hash VARCHAR(1024) NOT NULL,
    role VARCHAR(10) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now() 
);

CREATE TABLE posts(
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    content TEXT NOT NULL,
    img_name VARCHAR(500),
    img_path VARCHAR(500),
    img_expiration_date TIMESTAMPTZ,
    likes INT DEFAULT 0,
    user_id UUID REFERENCES users(id),
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now() 
);

CREATE TABLE count_posts(
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    username VARCHAR(124) UNIQUE NOT NULL,
    count_posts INT DEFAULT 0
);

CREATE TABLE blacklist_tokens(
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    jti VARCHAR(36) NOT NULL UNIQUE
);