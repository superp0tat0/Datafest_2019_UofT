library(tidyverse)
dinesafe = read_csv("./gps.csv")
RPE = read_csv("./rpe.csv")
game = read_csv("./games.csv")
features = read_csv("./Mydata.csv")

Distance = dinesafe %>% 
  group_by(GameID,PlayerID) %>% 
  summarise(Total_Distance = 0.1 * sum(Speed, na.rm = TRUE)) %>% 
  arrange(desc(Total_Distance))

Inner_Join_Game_Distance = dplyr::inner_join(game,Distance,RPE,by="GameID")
Game_Distance_Sim = Inner_Join_Game_Distance %>% select(GameID,PlayerID,Total_Distance)
Inner_Join_Game_RPE = dplyr::inner_join(game,RPE,by="Date")
Game_RPE_Sim = Inner_Join_Game_RPE %>% select(GameID,PlayerID,RPE)
Inner_Join_All = dplyr::inner_join(Game_Distance_Sim,Game_RPE_Sim,by=c("GameID","PlayerID"))

Final_result_pre = Inner_Join_All %>% group_by(GameID,PlayerID,Total_Distance) %>% summarise(AVG_RPE = mean(RPE))
Training_Sets_preprocess = inner_join(Final_result,features,by=c("GameID","PlayerID"))

write.csv(Final_result,"Result.csv")
write.csv(Distance,'Distance.csv')
write.csv(Training_Sets_preprocess,'Training_sets.csv')