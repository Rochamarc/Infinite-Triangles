class Line:
    def __init__(self, a: list[int, int], b: list[int, int]) -> None:
        """

        Parameters
        ----------
        a : list[int, int]
            Cartesian coordinates for point a

        b : list[int, int]
            Cartesian coordinates for point b
        """
        
        self.x1, self.y1 = a[0], a[-1]
        self.x2, self.y2 = b[0], b[-1]

        self.m = None 
        self.n = None 

        self.equation_line()

    def __repr__(self):
        # signal = '+' if self.n >= 0 else ''
        if self.n >= 0:    
            return f"y = {self.m}*x +{self.n}"
        return f"y = {self.m}*x {self.n}"
    
    def equation_line(self) -> None:
        """Calculates the equation of the straight line and defines the value of m & n
        
        * y = m.x + n
        """

        # calculates m & n based on the formula m = y2 - y1 / x2 - x1 & y - y1 = m * (x - x1)
        try:
            m = (self.y2 - self.y1)/(self.x2 - self.x1) 
        except ZeroDivisionError:
            m = 0
            
        n = (m * -self.x1) + self.y1
        
        self.m = m 
        self.n = n

        return None 
    
    def calculates_x(self, x: int) -> int | float:
        """Calculates the value of x in the x coordinate

        Returns
        -------
        int | float : Value of the m*x + n
        """

        return self.m * x + self.n
    
    def middle_point(self) -> list[int, int]:
        """Calculates the x and y middle point of the line

        Returns
        -------
        list[int | float, int | float] : Cartesian coordinates to the middle point belonging to R² 
        """

        middle_x = (self.x1 + self.x2) / 2
        middle_y = self.calculates_x(middle_x)

        return [ middle_x, middle_y ]