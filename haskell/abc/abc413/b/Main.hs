import Control.Monad (replicateM)
import qualified Data.Set as S

main :: IO ()
main = do
  nLine <- getLine
  let n = read nLine :: Int

  raws <- replicateM n getLine

  print(solve n raws)

solve :: Int -> [String] -> Int
solve n strs = S.size (S.fromList [strs !! i ++ strs !! j | i <- [0..(n - 1)], j <- [0..(n - 1)], i /= j])
