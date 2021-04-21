import re
import glob
import os

class fileStats:
    
    rawLines = ''
    numLines = 0
    numCommentLines = 0
    numClasses = 0
    linesInClasses = 0
    linesNotInClasses = 0
    numMethods = 0
    linesInMethods = 0
    numParams = 0
    
    def __init__(self, fileName):
        
        #read file
        rawCode = self.readFile(fileName)
        
        #clean file
        lines = self.cleanFile(rawCode)
        
        #process file
        self.processFile(lines)
        
    def readFile(self, fileName):
        try:
            file = open(fileName)
            code = file.read()
            file.close()
        except:
            code = ""

        return code
    
    def cleanFile(self, codeString):
        return [l.replace('    ','tab ') for l in codeString.split('\n') if not l.isspace()]
    
    def getNumLines(self):
        
        return self.numLines
    
    def getNumCommentLines(self):
        
        return self.numCommentLines
    
    def getNumClasses(self):
        
        return self.numClasses
    
    def getNumMethods(self):
        
        return self.numMethods
    
    def getTotalParams(self):
        
        return self.numParams
    
    def getLinesInMethods(self):
        
        return self.linesInMethods
    
    def getLinesNotInClasses(self):
        
        return self.linesNotInClasses
    
    def getLinesInClasses(self):
        
        return self.linesInClasses
    
    def countCommentLines(self, rawLines):
        
        return len([l for l in rawLines if '#' in l])
    
    def getStarts(self, rawLines, token):
        return [rawLines.index(l) for l in rawLines if token in l]
    
    def getEnds(self, rawLines, starts):
        ends = []
        for s in starts:
            numTabs = rawLines[s].count('tab')
            for ind, value in enumerate(rawLines):
                if (ind > s):
                    if (value.count('tab') > numTabs):
                        continue
                    else:
                        ends.append(ind)
                        break

        return ends
    
    def getInsAndOuts(self, starts, ends, total):
        ins = sum([ends[i] - starts[i] for i in range(len(starts))])
        outs = total - ins

        return ins, outs
    
    def countMetrics(self, rawLines, token):
        
        starts = self.getStarts(rawLines, token)
        
        ends = self.getEnds(rawLines, starts)
        
        num = len(starts)
        
        ins, outs, = self.getInsAndOuts(starts, ends, len(rawLines))
        
        return num, ins, outs
    
    def getParams(self):
        
        lines = [self.rawLines[i] for i in self.getStarts(self.rawLines, 'def')]
        params = [re.search('\((.*)\)', l)[0][1:-1].split(',') for l in lines]
        params = list(filter(lambda x: x != 'self', [item for sublist in params for item in sublist]))
        
        return params
    
    def containsLoop(self, line):
        
        loopTypes = ['for','do','while']
        
        for loop in loopTypes:
            
            if (loop in line) and (':' in line):
                
                return True
            
        return False
        
    
    def getLoops(self):
        
        starts = [i for i in range(len(self.rawLines)) if self.containsLoop(self.rawLines[i])]
            
        ends = self.getEnds(self.rawLines, starts)
        
        return starts, ends
        
    
    def getNumNestedLoops(self):
        
        starts, ends = self.getLoops()
        
        count = 0
        
        for s, e in zip(starts, ends):
            
            count += len([c for c in self.rawLines[s+1:e] if self.containsLoop(c)])
            
        return count
    
    def getNumEnumerateIssues(self):
        
        count = 0
        
        starts, ends = self.getLoops()
        
        rangeLenLines = [self.rawLines[i] for i in starts if 'for' in self.rawLines[i] and 'range(len(' in self.rawLines[i]]
        
        lists = [r.split('range(len(')[-1].split(')')[0] for r in rangeLenLines]
        
        tokens = [r.split('for')[1].split('in')[0].strip() for r in rangeLenLines]
        
        for line, li, tok in zip(rangeLenLines, lists, tokens):
            
            ind = starts.index(self.rawLines.index(line))
            
            snippet = [s for s in self.rawLines[starts[ind]+1:ends[ind]] if li+'['+tok in s]
            
            if len(snippet) > 0:
                
                count += 1
                
        return count
            
            
    
    def processFile(self, lines):
        
        self.rawLines = lines 
        
        self.numLines = len(lines)
        
        self.numCommentLines = self.countCommentLines(lines)
        
        self.numClasses, self.linesInClasses, self.linesNotInClasses = self.countMetrics(lines, 'class')
        
        self.numMethods, self.linesInMethods, tmp = self.countMetrics(lines, 'def')
        
        self.numParams = len(self.getParams())