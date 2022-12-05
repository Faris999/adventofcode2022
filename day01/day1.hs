main = do
    contents <- readFile "input.txt"
    let fileLines = lines contents
    let integers = map read fileLines :: [Integer]
    print sum integers