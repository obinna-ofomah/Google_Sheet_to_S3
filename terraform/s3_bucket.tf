resource "aws_s3_bucket" "gsheet_bucket" {
  bucket = "obinna-gsheet-bucket"

  tags = {
    Name        = "Students"
    Environment = "Education"
  }
}