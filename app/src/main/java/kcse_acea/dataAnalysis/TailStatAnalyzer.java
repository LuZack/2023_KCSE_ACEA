package kcse_acea.dataAnalysis;

import java.io.File;
import java.io.FileWriter;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.stream.StreamSupport;

import com.google.common.collect.Iterables;
import kcse_acea.Main;
import kcse_acea.change.ChangeData;
import kcse_acea.diffTool.GumTreeRunner;
import kcse_acea.miners.ChangeMiner;
import kcse_acea.miners.CommitMiner;
import org.apache.commons.collections4.IterableUtils;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;

public class TailStatAnalyzer {
    public TailStatAnalyzer(Reader reader) {
        String fileKey = Main.getPath().substring(Main.getPath().lastIndexOf("/")+1, Main.getPath().lastIndexOf("."));
        HashMap<Integer, Integer> tailStat = new HashMap<>();
        try {
            List<CSVRecord> records = CSVFormat.RFC4180.parse(reader).getRecords();
            File statFile = new File(System.getProperty("user.dir")+"/statistics/stat_"+fileKey+".csv");
            File hashIndexFile = new File(System.getProperty("user.dir")+"/statistics/index_"+fileKey+".csv");
            statFile.createNewFile();
            hashIndexFile.createNewFile();
            FileWriter statWriter = new FileWriter(statFile);
            FileWriter hashIndexWriter = new FileWriter(hashIndexFile);
            int recordSize = records.size();

            int progressCount = 1;
            for (CSVRecord record : records) {
                String hash = record.get(0);
                int clusterSize = record.size()-1;
                int count = 0;
                for (String content: record.toList()) {
                    try {
                        if (count++ != 0) {
                            String [] project_commit_path = content.split("&");
                            String [] company_project = project_commit_path[0].split("~");
                            String path = company_project[0] + "/" + company_project[1];
                            CommitMiner commitMiner = new CommitMiner(path, true);
                            ChangeMiner changeMiner = new ChangeMiner();
                            changeMiner.setProperties(path, commitMiner.getRepo(), "JAVA", "GUMTREE");
                            String clusterTitle = changeMiner.collect(path, project_commit_path[2], commitMiner.getCommit(path,project_commit_path[1]), commitMiner.getRepo());
                            if (clusterTitle.length() > 10) {
                                hashIndexWriter.write(hash + " " + clusterTitle+ "\n");

                                int tail_length = clusterTitle.split("|").length;
                                if (tailStat.get(tail_length) == null)
                                    tailStat.put(tail_length,clusterSize);
                                else
                                    tailStat.put(tail_length, tailStat.get(tail_length)+clusterSize);
                                System.out.println(progressCount++/recordSize*100 + "% done :" + progressCount + "/" + recordSize);
                                break;
                            }
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }

                }
            }
            hashIndexWriter.flush();
            hashIndexWriter.close();

            for (int j = 1; j <= tailStat.size(); j++) {
                if (!tailStat.keySet().contains(j) || tailStat.get(j) == null)
                    continue;

                statWriter.write(j + "," +tailStat.get(j) +"\n");
            }
            statWriter.flush();
            statWriter.close();

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
