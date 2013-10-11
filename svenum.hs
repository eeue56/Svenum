module Svenum
where

	import Data.Map
	import Data.Char

	data AbstractType = Number String | Text String | Other String deriving (Show, Eq)

	guessType :: String -> AbstractType
	guessType xs 
		| all (\x -> isDigit x || x == '.') xs = Number xs
		| otherwise = Text xs



	main = do
		putStrLn $ show $ guessType "2356"
		putStrLn $ show $ guessType "2345.235"
		putStrLn $ show $ guessType "23523...2334"
		putStrLn $ show $ guessType "3434,3234"
		putStrLn $ show $ guessType "hello"
		putStrLn $ show $ guessType "hello123"

		let m = constructMap [1, 2] [3, 4]

		putStrLn $ show $ findValue m "Hello"




