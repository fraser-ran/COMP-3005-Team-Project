CREATE TABLE Publisher(
    p_id int,
    name varchar(255),
    address varchar(255),
    email varchar(255),
    phone_number varchar(255),
    bank_account int,
    PRIMARY KEY(p_id)
);

CREATE TABLE Book(
    isbn int,
    title varchar(255),
    publisher varchar(255),
    author_name varchar(255),
    genre varchar(255),
    num_pages int,
    price int,
    quantity int,
    PRIMARY KEY(isbn),
    FOREIGN KEY (publisher) REFERENCES Publisher(name)
);

CREATE TABLE Users(
    u_id int,
    username varchar(255),
    password varchar(255),
    email varchar(255),
    address varchar(255),
    country varchar(255),
    city varchar(255),
    postal_code varchar(6),
    card_name varchar(255),
    card_number int,
    ccv int,
    exp_date DATE,
    billing_street varchar(255),
    billing_city varchar(255),
    billing_country varchar(255),
    PRIMARY KEY(username)
);

CREATE TABLE Orders(
    o_id int,
    u_id int,
    date DATE,
    time TIME,
    cost int,
    PRIMARY KEY(o_id),
    FOREIGN KEY (u_id) REFERENCES Users(username)
);

CREATE TABLE Sales(
    isbn int,
    title varchar(255)
    publisher varchar(255),
    cost int,
    num_sold int,
    profits int,
    PRIMARY KEY(isbn),
    FOREIGN KEY (isbn) REFERENCES Book(isbn),
    FOREIGN KEY (title) REFERENCES Book(title),
    FOREIGN KEY (publisher) REFERENCES Book(publisher)
);