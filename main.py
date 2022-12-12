import sqlite3
from sqlite3 import Error

from sqlFunc import *






if __name__ == "__main__":

    insertBook(3, "Harry Potter: Philosopher's Stone","Bloomsbury", "J. K Rowling ", "Fantasy", 233, 12,25)
    insertBook(4, "Harry Potter: Chamber of Secrets","Bloomsbury", "J. K Rowling ", "Fantasy", 251, 12,25)
    insertBook(5, "Harry Potter: Prisoner of Azkaban","Bloomsbury", "J. K Rowling ", "Fantasy", 448, 15,25)
    insertBook(6, "Harry Potter: Goblet of Fire","Bloomsbury", "J. K Rowling ", "Fantasy", 636 , 15,25)
    insertBook(7, "Harry Potter: Order of the Phoenix","Bloomsbury", "J. K Rowling ", "Fantasy", 870, 17,25)
    insertBook(8, "Harry Potter: Half-Blood Prince","Bloomsbury", "J. K Rowling ", "Fantasy", 652, 17,25)
    insertBook(9, "Harry Potter: Deathly Hallows","Bloomsbury", "J. K Rowling ", "Fantasy", 607, 17,25)
    insertBook(10, "The Hobbit","Allen & Unwin", "J. R. R. Tolkien", "Fantasy", 295, 12,25)
    insertBook(11, "The Fellowship of the Ring","Allen & Unwin", "J. R. R. Tolkien", "Fantasy", 423, 15,25)
    insertBook(12, "The Two Towers","Allen & Unwin", "J. R. R. Tolkien", "Fantasy", 352, 15,25)
    insertBook(13, "The Return of the King","Allen & Unwin", "J. R. R. Tolkien", "Fantasy", 416, 15,25)
    insertBook(14, "The Silmarillion","Allen & Unwin", "J. R. R. Tolkien", "Fantasy", 432, 15,25)
    insertBook(15, "The Lord of the Rings","Allen & Unwin", "J. R. R. Tolkien", "Fantasy", 1216, 45,25)
    insertBook(16, "The Hitchhiker's Guide to the Galaxy","Pan Books", "Douglas Adams", "Science Fiction", 224, 12,25)
    insertBook(17, "The Restaurant at the End of the Universe","Pan Books", "Douglas Adams", "Science Fiction", 224, 12,25)
    insertBook(18, "Life, the Universe and Everything","Pan Books", "Douglas Adams", "Science Fiction", 224, 12,25)
    insertBook(19, "So Long, and Thanks for All the Fish","Pan Books", "Douglas Adams", "Science Fiction", 224, 12,25)
    insertBook(20, "Mostly Harmless","Pan Books", "Douglas Adams", "Science Fiction", 224, 12,25)
    insertBook(21, "Percy Jackson and the Lightning Thief","Disney-Hyperion", "Rick Riordan", "Fantasy", 377, 15,25)
    insertBook(22, "Percy Jackson and the Sea of Monsters","Disney-Hyperion", "Rick Riordan", "Fantasy", 377, 15,25)
    insertBook(23, "Percy Jackson and the Titan's Curse","Disney-Hyperion", "Rick Riordan", "Fantasy", 377, 15,25)
    insertBook(24, "Percy Jackson and the Battle of the Labyrinth","Disney-Hyperion", "Rick Riordan", "Fantasy", 377, 15,25)
    insertBook(26, "Percy Jackson and the Last Olympian","Disney-Hyperion", "Rick Riordan", "Fantasy", 377, 15,25)
    insertBook(27, "The Hunger Games","Scholastic Press", "Suzanne Collins", "Science Fiction", 374, 15,25)
    insertBook(28, "Catching Fire","Scholastic Press", "Suzanne Collins", "Science Fiction", 391, 15,25)
    insertBook(29, "Mockingjay","Scholastic Press", "Suzanne Collins", "Science Fiction", 400, 15,25)
    insertBook(30, "The Maze Runner","Delacorte Press", "James Dashner", "Science Fiction", 384, 15,25)
    insertBook(31, "The Scorch Trials","Delacorte Press", "James Dashner", "Science Fiction", 384, 15,25)
    insertBook(32, "The Death Cure","Delacorte Press", "James Dashner", "Science Fiction", 384, 15,25)
    insertBook(33, "The Kill Order","Delacorte Press", "James Dashner", "Science Fiction", 384, 15,25)
    insertBook(34, "The Maze Runner: The Fever Code","Delacorte Press", "James Dashner", "Science Fiction", 384, 15,25)
    insertBook(35, "The Hunger Games: The Official Illustrated Movie Companion","Scholastic Press", "Suzanne Collins", "Science Fiction", 384, 15,25)
    insertBook(36, "Dune","Chilton Books", "Frank Herbert", "Science Fiction", 604, 20,25)
    insertBook(37, "Dune Messiah","Chilton Books", "Frank Herbert", "Science Fiction", 604, 20,25)
    insertBook(38, "Children of Dune","Chilton Books", "Frank Herbert", "Science Fiction", 604, 20,25)
    insertBook(39, "God Emperor of Dune","Chilton Books", "Frank Herbert", "Science Fiction", 604, 20,25)
    insertBook(40, "Heretics of Dune","Chilton Books", "Frank Herbert", "Science Fiction", 604, 20,25)
    insertBook(41, "Chapterhouse: Dune","Chilton Books", "Frank Herbert", "Science Fiction", 604, 20,25)
    insertBook(43, "The Call of the Wild","Macmillan", "Jack London", "Adventure", 224, 12,25)
    insertBook(44, "The Sea Wolf","Macmillan", "Jack London", "Adventure", 224, 12,25)
    insertBook(45, "White Fang","Macmillan", "Jack London", "Adventure", 224, 12,25)
    insertBook(46, "The Iron Heel","Macmillan", "Jack London", "Adventure", 224, 12,25)
    insertBook(47, "The Star Rover","Macmillan", "Jack London", "Adventure", 224, 12,25)
    insertBook(48, "The Scarlet Pimpernel","Macmillan", "Baroness Orczy", "Adventure", 224, 12,25)
    insertBook(49, "The Prisoner of Zenda","Macmillan", "Anthony Hope", "Adventure", 224, 12,25)
    insertBook(50, "The Witcher", "The Hatchet Group", "Andrzej Sapkowski", "Fantasy", 384, 15,25)
    insertBook(51, "The Last Wish", "The Hatchet Group", "Andrzej Sapkowski", "Fantasy", 384, 15,25)
    insertBook(52, "Sword of Destiny", "The Hatchet Group", "Andrzej Sapkowski", "Fantasy", 384, 15,25)
    insertBook(53, "Blood of Elves", "The Hatchet Group", "Andrzej Sapkowski", "Fantasy", 384, 15,25)
    insertBook(54, "Time of Contempt", "The Hatchet Group", "Andrzej Sapkowski", "Fantasy", 384, 15,25)
    insertBook(55, "Baptism of Fire", "The Hatchet Group", "Andrzej Sapkowski", "Fantasy", 384, 15,25)
    insertBook(56, "The Tower of Swallows", "The Hatchet Group", "Andrzej Sapkowski", "Fantasy", 384, 15,25)
    insertBook(57, "Lady of the Lake", "The Hatchet Group", "Andrzej Sapkowski", "Fantasy", 384, 15,25)
    insertBook(58, "Season of Storms", "The Hatchet Group", "Andrzej Sapkowski", "Fantasy", 384, 15,25)
    insertBook(59, "A Game of Thrones", "Bantam Books", "George R. R. Martin", "Fantasy", 864, 30,25)
    insertBook(60, "A Clash of Kings", "Bantam Books", "George R. R. Martin", "Fantasy", 864, 30,25)
    insertBook(61, "A Storm of Swords", "Bantam Books", "George R. R. Martin", "Fantasy", 864, 30,25)
    insertBook(62, "A Feast for Crows", "Bantam Books", "George R. R. Martin", "Fantasy", 864, 30,25)
    insertBook(63, "A Dance with Dragons", "Bantam Books", "George R. R. Martin", "Fantasy", 864, 30,25)
    insertBook(64, "The Winds of Winter", "Bantam Books", "George R. R. Martin", "Fantasy", 864, 30,25)
    insertBook(65, "A Dream of Spring", "Bantam Books", "George R. R. Martin", "Fantasy", 864, 30,25)
    insertBook(66, "LeBron James Auto-Biography", "Los Angelos Lakers", "LeBron James", "Sports", 1000, 30,25)
    insertBook(67, "James Harden Auto-Biography", "Houston Rockets", "James Harden", "Sports", 1000, 30,25)
    pass


