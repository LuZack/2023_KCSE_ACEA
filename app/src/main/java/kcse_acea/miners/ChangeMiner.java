package kcse_acea.miners;

import java.util.List;


import kcse_acea.change.ChangeData;
import kcse_acea.diffTool.GumTreeRunner;
import kcse_acea.utils.RepoUtils;
import org.eclipse.jgit.diff.DiffEntry;
import org.eclipse.jgit.lib.Repository;
import org.eclipse.jgit.revwalk.RevCommit;


public class ChangeMiner {
    private Repository repo;
    private String DiffTool = "GUMTREE";
    private String fileExtension;
    private String filePath;
    private String Java = ".java";
    private String Python = ".py";
    private String C = ".c";
    public static int count;


    public void setProperties(String filePath, Repository repo, String language, String DiffTool) {
        this.filePath = filePath;
        this.repo = repo;
        this.DiffTool = DiffTool;
        switch(language.toUpperCase()) {
            case "PYTHON":
                fileExtension = Python;
                break;
            case "C":
                fileExtension = C;
                break;
            default:
                fileExtension = Java;
        }
    }


    public String collect(String filePath, String fileName, RevCommit commit, Repository repo) {
        if (commit.getParentCount() < 1) return "";
        RevCommit parent = commit.getParent(0);
        List<DiffEntry> diffs = RepoUtils.diff(parent, commit, repo);
        for (DiffEntry diff : diffs) {
            try {
                String oldPath = diff.getOldPath();
                String newPath = diff.getNewPath();
                if (fileName.endsWith(".py")) fileExtension = Python;
                else if (fileName.endsWith(".c")) fileExtension = C;
                else fileExtension = Java;
                if (!newPath.equals(fileName) || newPath.indexOf("Test") >= 0 || !newPath.endsWith(fileExtension)) continue;
                String srcFileSource = RepoUtils.fetchBlob(repo, commit.getId().getName() + "~1", oldPath);
                String dstFileSource = RepoUtils.fetchBlob(repo, commit.getId().getName(), newPath);
                ChangeData changeData = new ChangeData();
                switch (DiffTool) {
                    default:
                        GumTreeRunner gumtree = new GumTreeRunner(filePath, fileExtension, srcFileSource, dstFileSource);
                        changeData = gumtree.constructChange(changeData);
                }
                return changeData.getActions();
//				changeInfo.generateMap(changeData, DiffTool, commit.getId().getName(), newPath);
//				if (changeInfo.getTotalCount() > 0 && changeInfo.getTotalCount()%200000==0) {
//					changeInfo.printStatistic();
//				}
            } catch (Exception e) {
                e.printStackTrace();
                continue;
            }
        }
        return "";
    }
}


