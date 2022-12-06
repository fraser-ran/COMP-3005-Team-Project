CREATE TABLE Book(
    isbn int,
    title varchar(255),
    publisher varchar(255),
    author_name varchar(255),
    genre varchar(255),
    num_pages int,
    price int,
    PRIMARY KEY(isbn)
);

CREATE TABLE Publisher(
    p_id int,
    name varchar(255),
    address varchar(255),
    email varchar(255),
    phone_number varchar(255),
    bank_account int,
    PRIMARY KEY(p_id)
);


CREATE TABLE Sales(
    s_id int,
    date DATE,
    time TIME,
    cost int,
    PRIMARY KEY(s_id)
);

CREATE TABLE Customer(
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
    PRIMARY KEY(u_id)
);

create table cusomter-sales
	(s_id			CHAR(9), 
	 u_id			CHAR(9),
	 primary key (s_id, u_id),
	 foreign key (u_id) references cusomter,
	 foreign key (s_id) references sales
	);

create table book-sales
	(s_id			CHAR(9), 
	 ISBN			CHAR(9),
	 primary key (s_id, ISBN),
	 foreign key (ISBN) references book,
	 foreign key (s_id) references sales
	);

create table sales-publisher	
	(s_id			CHAR(9), 
	 p_id			CHAR(9),
	 primary key (s_id, p_id),
	 foreign key (p_id) references publisher,
	 foreign key (u_id) references sales
	);