library(corrplot)
Training_Sets<-read_csv("Training_sets.csv")
head(Training_Sets)
X = as.matrix(Training_Sets[,1:14])
Cor = as.matrix(Training_Sets)
fit=manova(X ~ Training_Sets$Total_Distance)
summary(fit, test="Hotelling-Lawley")
res <- cor(X)
res2 <- cor(Cor)
corrplot(res, type = "upper", order = "hclust", 
         tl.col = "black", tl.srt = 45)
corrplot(res2, type = "upper", order = "hclust", 
         tl.col = "black", tl.srt = 45)

