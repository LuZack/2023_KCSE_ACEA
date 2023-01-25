package kcse_acea.dataAnalysis;

import java.io.File;
import java.io.FileWriter;
import java.io.Reader;
import java.util.ArrayList;
import java.util.HashMap;

import kcse_acea.change.ChangeData;
import kcse_acea.diffTool.GumTreeRunner;
import kcse_acea.miners.ChangeMiner;
import kcse_acea.miners.CommitMiner;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;

public class TailStatAnalyzer {
    public TailStatAnalyzer(Reader reader) {
        HashMap<Integer, Integer> tailStat = new HashMap<>();
        try {
            Iterable<CSVRecord> records = CSVFormat.RFC4180.parse(reader);
            File statFile = new File(System.getProperty("user.dir")+"/statistics/stat.csv");
            File hashIndexFile = new File(System.getProperty("user.dir")+"/statistics/index.csv");
            statFile.createNewFile();
            hashIndexFile.createNewFile();
            FileWriter statWriter = new FileWriter(statFile);
            FileWriter hashIndexWriter = new FileWriter(hashIndexFile);

            for (CSVRecord record : records) {
                String hash = record.get(0);
                int clusterSize = record.size()-1;
                int count = 0;
                for (String content: record.toList()) {
                    if (count++ != 0) {
                        String [] project_commit_path = content.split("&");
                        String [] company_project = project_commit_path[0].split("~");
                        String path = company_project[0] + "/" + company_project[1];
                        CommitMiner commitMiner = new CommitMiner(path, true);
                        ChangeMiner changeMiner = new ChangeMiner();
                        changeMiner.setProperties(path, commitMiner.getRepo(), "JAVA", "GUMTREE");
                        String clusterTitle = changeMiner.collect(path, project_commit_path[2], commitMiner.getCommit(path,project_commit_path[1]), commitMiner.getRepo());
                        if (clusterTitle.length() > 10) {
                            statWriter.write(hash + " " + clusterTitle+ "\n");

                            int tail_length = clusterTitle.split("|").length;
                            if (tailStat.get(tail_length) == null)
                                tailStat.put(tail_length,clusterSize);
                            else
                                tailStat.put(tail_length, tailStat.get(tail_length)+clusterSize);
                            break;
                        }
                    }
                }

            }
            for (int j = 1; j <= tailStat.size(); j++) {
                if (tailStat.get(j) == null)
                    continue;

                hashIndexWriter.write(j + "," +tailStat.get(j) +"\n");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
