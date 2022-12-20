import Data.List

decrypt :: [Int] -> [Int]
decrypt = id

-- moves element at index a to index b
move :: Int -> Int -> [Int] -> [Int]
move a b list = insertAt (list !! a) b . removeAt a $ list

enumerate :: [Int] -> [(Int, Int)]
enumerate = zip [0..]

removeAt :: Int -> [Int] -> [Int]
removeAt index  = map snd . filter (\(i, _) -> i /= index) . enumerate

insertAt :: Int -> Int -> [Int] -> [Int]
insertAt el 0 xs = el : xs
insertAt el i (x:xs) = x : insertAt el (i-1) xs

-- elemIndex idx list


main = do
    input <- readFile "test.txt"
    let encrypted = map read $ lines input
    let decrypted = move 0 2 encrypted
    print decrypted