import json
MODULE = 'qorts'

mi_template_json = {'module_version': '00.00.00', 'program_name': 'qorts', 'program_subname': '', 'program_version': '3.8', 'compute': {'environment': 'aws', 'language': 'R', 'language_version': '4.1', 'vcpus': 2, 'memory': 6000}, 'program_arguments': '--stranded --generatePdfReport', 'program_input': [{'input_type': 'file', 'input_file_type': 'BAM', 'input_position': -2, 'input_prefix': ''}], 'program_output': [{'output_type': 'folder', 'output_file_type': '', 'output_position': -1, 'output_prefix': ''}], 'alternate_inputs': [{'input_type': 'file', 'input_file_type': 'GTF', 'input_position': -2, 'input_prefix': ''}], 'alternate_outputs': [], 'defaults': {}}
with open(MODULE+'.template.json','w') as fout:
    json.dump(mi_template_json, fout)

io_dryrun_json = {'input': ['s3://hubtenants/test/rnaseq/run_test1/rnastar/rnastar_test_tiny1.Aligned.sortedByCoord.out.bam'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/qorts/rnastar_test_tiny1/'],  'alternate_inputs': ['s3://hubgenomes/genomes/mm10/mm10.canonical.ensGene.gtf'], 'alternate_outputs': [], 'program_arguments': '--stranded --generatePdfReport', 'sample_id': 'rnastar_test_tiny1', 'dryrun': ''}
io_json = {'input': ['s3://hubtenants/test/rnaseq/run_test1/rnastar/rnastar_test_tiny1.Aligned.sortedByCoord.out.bam'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/qorts/rnastar_test_tiny1/'],  'alternate_inputs': ['s3://hubgenomes/genomes/mm10/mm10.canonical.ensGene.gtf'], 'alternate_outputs': [], 'program_arguments': '--stranded --generatePdfReport', 'sample_id': 'rnastar_test_tiny1'}
io_json2 = {'input': ['s3://hubtenants/test/rnaseq/run_test1/rnastar/rnastar_test_tiny2.Aligned.sortedByCoord.out.bam'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/qorts/rnastar_test_tiny2/'],  'alternate_inputs': ['s3://hubgenomes/genomes/mm10/mm10.canonical.ensGene.gtf'], 'alternate_outputs': [], 'program_arguments': '--stranded --generatePdfReport', 'sample_id': 'rnastar_test_tiny2'}
io_json3 = {'input': ['s3://hubtenants/test/rnaseq/run_test1/rnastar/rnastar_test_tiny3.Aligned.sortedByCoord.out.bam'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/qorts/rnastar_test_tiny3/'],  'alternate_inputs': ['s3://hubgenomes/genomes/mm10/mm10.canonical.ensGene.gtf'], 'alternate_outputs': [], 'program_arguments': '--stranded --generatePdfReport', 'sample_id': 'rnastar_test_tiny3'}
io_json4 = {'input': ['s3://hubtenants/test/rnaseq/run_test1/rnastar/rnastar_test_tiny4.Aligned.sortedByCoord.out.bam'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/qorts/rnastar_test_tiny4/'],  'alternate_inputs': ['s3://hubgenomes/genomes/mm10/mm10.canonical.ensGene.gtf'], 'alternate_outputs': [], 'program_arguments': '--stranded --generatePdfReport', 'sample_id': 'rnastar_test_tiny4'}
io_json5 = {'input': ['s3://hubtenants/test/rnaseq/run_test1/rnastar/rnastar_test_tiny5.Aligned.sortedByCoord.out.bam'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/qorts/rnastar_test_tiny5/'],  'alternate_inputs': ['s3://hubgenomes/genomes/mm10/mm10.canonical.ensGene.gtf'], 'alternate_outputs': [], 'program_arguments': '--stranded --generatePdfReport', 'sample_id': 'rnastar_test_tiny5'}
io_json6 = {'input': ['s3://hubtenants/test/rnaseq/run_test1/rnastar/rnastar_test_tiny6.Aligned.sortedByCoord.out.bam'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/qorts/rnastar_test_tiny6/'],  'alternate_inputs': ['s3://hubgenomes/genomes/mm10/mm10.canonical.ensGene.gtf'], 'alternate_outputs': [], 'program_arguments': '--stranded --generatePdfReport', 'sample_id': 'rnastar_test_tiny6'}

with open(MODULE+'.dryrun_test.io.json','w') as fout:
    json.dump(io_dryrun_json, fout)
with open(MODULE+'.test.io.json','w') as fout:
    json.dump(io_json, fout)
with open(MODULE+'.test.io2.json','w') as fout:
    json.dump(io_json2, fout)
with open(MODULE+'.test.io3.json','w') as fout:
    json.dump(io_json3, fout)
with open(MODULE+'.test.io4.json','w') as fout:
    json.dump(io_json4, fout)
with open(MODULE+'.test.io5.json','w') as fout:
    json.dump(io_json5, fout)
with open(MODULE+'.test.io6.json','w') as fout:
    json.dump(io_json6, fout)    
    
# job info test JSONs                                                                                                        
job_json = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://hubseq-data/modules/"+MODULE+"/job/"+MODULE+".test.io.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
job_json2 = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://hubseq-data/modules/"+MODULE+"/job/"+MODULE+".test.io2.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
job_json3 = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://hubseq-data/modules/"+MODULE+"/job/"+MODULE+".test.io3.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
job_json4 = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://hubseq-data/modules/"+MODULE+"/job/"+MODULE+".test.io4.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
job_json5 = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://hubseq-data/modules/"+MODULE+"/job/"+MODULE+".test.io5.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
job_json6 = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://hubseq-data/modules/"+MODULE+"/job/"+MODULE+".test.io6.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
with open(MODULE+'.test.job.json','w') as fout:
    json.dump(job_json, fout)
with open(MODULE+'.test.job2.json','w') as fout:
    json.dump(job_json2, fout)
with open(MODULE+'.test.job3.json','w') as fout:
    json.dump(job_json3, fout)
with open(MODULE+'.test.job4.json','w') as fout:
    json.dump(job_json4, fout)
with open(MODULE+'.test.job5.json','w') as fout:
    json.dump(job_json5, fout)
with open(MODULE+'.test.job6.json','w') as fout:
    json.dump(job_json6, fout)    
    
