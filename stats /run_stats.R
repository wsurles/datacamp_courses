
library(googlesheets)
library(rmarkdown)

##| Get data from google spreadsheet

# choose spreadsheet
gs <- gs_title("datacamp_statistics")

# list worksheets
gs_ws_ls(gs)

# load data from worksheet
df_william <- gs_read(ss = gs, ws = "william")
saveRDS(df_william, file = "data_william")

df_russell <- gs_read(ss = gs, ws = "russell")
saveRDS(df_russell, file = "data_russell")

##| Run notebook
render("datacamp_stats.Rmd")


