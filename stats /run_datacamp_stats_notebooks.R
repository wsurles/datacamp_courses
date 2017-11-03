
library(googlesheets)
library(rmarkdown)
library(dplyr)
library(lubridate)

gs <- gs_title("datacamp_statistics")
students <- gs_ws_ls(gs)

for (student in students) {

  ## Load data and run Notebook   
  # student = 'william'
  df_stats <- gs_read(ss = gs, ws = student)
  
  render(
    input = "datacamp_stats.Rmd",
    output_file = str_c("datacamp_stats_", student, ".html")
    )

}




