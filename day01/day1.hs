import Data.List

process :: [String] -> [[String]]
process [] = []
process a = (takeWhile (/= "") a) : (process (case dropWhile (/= "") a of
                                        [] -> []
                                        (x:xs) -> xs))

process' :: [[String]] -> [Int]
process' x = map (sum . map read) x

-- process'' :: [String] -> [Int]
-- process'' a = (sum $ map read (takeWhile (/= "") a)) : (process'' (case dropWhile (/= "") a of
                                        -- [] -> []
                                        -- (x:xs) -> xs))

main :: IO ()
main = do
    input <- readFile "input.txt"
    let fileLines = lines input
    let x = process fileLines
    let y = process' x
    let calories = reverse $ sort $ y
    putStrLn $ show $ head calories
    putStrLn $ show $ sum $ take 3 calories