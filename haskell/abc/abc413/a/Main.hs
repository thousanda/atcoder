main :: IO ()
main = do
  line1 <- getLine
  let [n, m] = map read (words line1) :: [Int]

  line2 <- getLine
  let as = map read (words line2) :: [Int]

  putStrLn (solve m as)

solve :: Int -> [Int] -> String 
solve cap nums
  | total <= cap = "Yes"
  | otherwise    = "No"
  where
    total = sum(nums)
