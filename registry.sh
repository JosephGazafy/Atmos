#!/bin/bash
ID=$(md5sum <<< "$(Josephgazafy)" | cut -c 1-8)
curl -X POST -d "{\"content\": \"✅ Node $ID Active\"}" https://discord.com/api/webhooks/1451503705953140890/KsrxKw4py4o0SCPFC4q02Xbf59ndVnlPEKoEqftnn0A93zWwSoNbjfnskvWB8DPzw884

