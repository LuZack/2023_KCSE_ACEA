package kcse_acea.dataAnalysis;

import java.io.File;
import java.io.Reader;

import kcse_acea.change.ChangeData;
import kcse_acea.diffTool.GumTreeRunner;
import kcse_acea.miners.ChangeMiner;
import kcse_acea.miners.CommitMiner;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;

public class TailStatAnalyzer {
    public TailStatAnalyzer(Reader reader) {
        try {
            Iterable<CSVRecord> records = CSVFormat.RFC4180.parse(reader);
            for (CSVRecord record : records) {
                String Hash = record.get(0);
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
                        System.out.println(clusterTitle);
                    }
                }

            }
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
