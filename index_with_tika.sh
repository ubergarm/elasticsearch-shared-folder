#/bin/bash
# TARGET="http://www.digilife.be/quickreferences/QRC/The%20One%20Page%20Linux%20Manual.pdf"
TARGET="./sample.rtf"

curl -X DELETE http://localhost:9200/test_attachments 

echo;
curl -X POST http://localhost:9200/test_attachments -d '{
    "mappings" : {
        "document" : {
            "properties" : {
                "content" : {
                    "type" : "attachment",
                    "fields" : {
                        "content"  : { "store" : "yes" },
                        "author"   : { "store" : "yes" },
                        "title"    : { "store" : "yes", "analyzer" : "english"},
                        "date"     : { "store" : "yes" },
                        "keywords" : { "store" : "yes", "analyzer" : "keyword" },
                        "_name"    : { "store" : "yes" },
                        "_content_type" : { "store" : "yes" }
                    }
                }
            }          
        }
    }
}'
 
echo;
echo '>>> Index a local document'
curl -i -X PUT http://localhost:9200/test_attachments/document/1 -d "{
    \"_name\" : \"$TARGET\",
    \"content\" : \"$(openssl base64 -in $TARGET)\"
}"

#java -jar /tmp/tika-app-1.4.jar -j $TARGET

# echo '>>> Index a remote document'
# curl -i -X PUT http://localhost:9200/test_attachments/document/1 -d "{
# echo;
# curl -X POST http://localhost:9200/test_attachments/_refresh
 
echo; echo ">>> Search..."
# curl "http://localhost:9200/test_attachments/_search?pretty=true&q=content.author:john&fields=content.title,content.author"
# curl "http://localhost:9200/test_attachments/_search?pretty=true&q=_all:linux"
# curl "http://localhost:9200/test_attachments/_search?pretty=true&q=_all:linux"
curl -XGET 'http://localhost:9200/test_attachments/_search' -d '{
    "query" : {
        "match_all" : {}
    }
}'
echo;
