# asiayo_test

綜合應用測驗

題目一:
word_count.py
利用迴圈逐一檢查每個單字，並使用字典統計每個單字出現的次數。完成統計再利用另一個迴圈找出次數最多的單字，最後輸出該單字及出現次數。

題目二:
Manifests Folder
k8s MySQL HA 部屬參數

題目三:
class_query.sh
SQL查詢語句

情境實戰測驗
題目一:
再不更改任何架構的前提下，先行確保所有服務皆為高可用性至少為2台以上，其中包含Web Server(Frontend), AP Server(Backend), Cache Server(Redis or Memcache), DB Server
並確認目前所有Server使用狀態(包含Connection、Session), 評估以往高峰期間的流量以及使用資源來進行評估是否調整Instance type以作為活動開始前置準備，並啟用Auto Scaling服務以避免
大量訪問時服務不中斷或是資源滿載而響應過慢，但在Auto Scaling啟用時需注意設置的啟動閥值以及擴展上限避免使用成本暴增，使用AutoScaling可以自動化進行部屬，可以避免響應實際響應速度過慢。

題目二:
因為是回應時間逾時，初期不確定問題出現在甚麼地方或是在哪個區域，初期會先確認網路層的問題，需要確認服務是部屬在哪，部屬的型態是All internal或是有進行跨Zone進行部屬, 網路連線若是沒有任何問題，開始進行異常Server的問題排查，例如:使用資源是否滿載(CPU、Memory、Disk Usage、IO...等), 另外確認目前該異常Server中的Session數量或Connection數量是否占用過多，觸及到服務設定的上限值，若全部都沒問題最終才來查看是否程式的響應與其他Node不同，例如:列隊響應時間過長...等。

題目三:
若已經排除網路問題以及防火牆規則阻擋問題，則可以使用ssh -vvv參數輸出詳細連線情形來進行確認連線異常的問題點，多數問題發生的可能性如下
1.SSH服務異常或被關閉 (雲端可使用Console or Session Manager, 地端則是可以從VM Console or 到現場接KVM連線進行服務重啟)
2.SSH服務端口被更改了 (雲端可使用Console or Session Manager, 地端則是可以從VM Console or 到現場接KVM連線確認服務端口)
3.機器主目錄(系統根目錄)硬碟空間滿載，評估是否執行重啟Server釋放暫存可以SSH遠端後，盡速確認占用資料並執行清除，若重啟後還是無法連線甚至Console也同樣無法操作
則可重新起一台Server並將原異常Server的Data磁區卸載並至新Server進行掛載進行修復。

題目四:
先假設ELK都已經安裝並且設定完成，下一步開始與開發團隊討論需要輸出的並且可以直觀判斷的Log並儲存在指定的Server或Local Server指定路徑下, 並在該處安裝beats or filebeat將Log傳送至接收端(可能是ElasticSearch或是Logstash), 如果直接傳送到ElasticSearch則可能需要再filebeat處進行Log解析與整理後進行傳送, 但如果filebeat是安裝在服務中的此作業可能造成服務中的Server使用資源過載，所以建議另外安裝Logstash來進行Log分析與整理，且Logstash擁有更多的Plugin可以導入分析多方向的Log data, 更輕量化更靈活的運用不同類型的plugin來達成log的型態置換、新增刪除或是新增備註日期...等。
