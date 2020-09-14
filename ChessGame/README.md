# Chess Game

---

---

## Classes

---

### Board Class

#### Board Methods

- make_board
- clear_board

#### Board Attributes

- collection of square instances
- ~~??? collection of piece instances?~~
  - !!!OR on square instance
  - OR just have their own position and don't need to live on a square

---

### Square Class

#### Square Methods

- is_occuppied?
- occupant_color?
- occupant_type?

#### Square Attributes

- position of each square
- get_color - sets is_white attribute to proper boolean
  - init method calls get_color method
- ??? a piece?
  - (see board class - can have piece live on a square, or live in board class as a collection with a separate but same position as relevant square - difference is that it doesn't actually "belong" to that square - is independent. Might be better for SRP/law of demeter purposes - don't know.)

---

### Game Class

#### Game Methods

- start_game
  - makes board, makes pieces, places pieces
- clear_board
- something for winner

#### Game Attributes

- board
- players
- player turn?

---

### Player Class

#### Player Methods

- None

#### Player Attributes

- player_name
- is_white bool - determines if they go first

---

### Piece Class

- piece types inherit from this general class

#### Piece Methods

- None?
  - movement methods are on piece type class which inherits from this class

#### Piece Attributes

- position
  - or store on square and have square contain piece
  - probably better if they are decoupled
- color
  - could be is_white bool
- is_captured - should be property with getter and setter
  - boolean - if true we don't render the piece
  - also have is_captured method - setter method
    - sets position to None and is_captured to true
- type
  - type refers to a class with no initializer.
  - the purpose of the type class is to provide methods that check the validity of desired moves

---

### Type Class (classes for Rook, Knight, Bishop, King, Queen, Pawn)

- no initializer
- does NOT (?) inherit from piece class. The board contains piece instances. Each piece instance references the corresponding type of that piece. On the referenced type exist methods for checking move validity based on the board

#### Type Methods

- is_valid_move
- valid_moves (maybe for providing a visualization of possible spots based on piece type - good for teaching chess to youngins)

#### Type Attributes

- None?
