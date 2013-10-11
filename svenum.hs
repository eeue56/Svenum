module Svenum
where

	import Data.Char

	data AbstractType = Number String | Text String | Other String


	guessType :: String -> AbstractType
	guessType xs 
		| all $ isDigit xs = Number xs
		| otherwise = Text xs


	
