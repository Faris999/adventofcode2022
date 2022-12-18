import Data.List

process :: [String] -> [[String]]
process [] = []
process a = takeWhile (/= "") a : process (case dropWhile (/= "") a of
                                        [] -> []
                                        (x:xs) -> xs)

process' :: [[String]] -> [Int]
process' = map (sum . map read)

process'' :: [String] -> [Int]
process'' = process' . process

main :: IO ()
main = do
    input <- readFile "input.txt"
    let fileLines = lines input
    let y = process'' fileLines
    let calories = reverse $ sort y
    print $ head calories
    print $ sum $ take 3 calories