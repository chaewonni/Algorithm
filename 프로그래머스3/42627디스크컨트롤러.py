import heapq

def solution(jobs):
    # 요청 시각 기준으로 정렬
    jobs.sort(key=lambda x: x[0])
    
    # 현재 시점, 반환 시간 합계, 대기 큐 초기화
    current_time = 0
    total_turnaround_time = 0
    waiting_queue = []
    job_index = 0
    num_jobs = len(jobs)
    
    while job_index < num_jobs or waiting_queue:
        # 현재 시점에 요청된 작업을 모두 대기 큐에 추가
        
        while job_index < num_jobs and jobs[job_index][0] <= current_time:
            # heap에도 (a,b) 이런식으로 넣을 수 있구나
            heapq.heappush(waiting_queue, (jobs[job_index][1], jobs[job_index][0])) #소요시간, 요청시간 순으로
            job_index += 1
        
        if waiting_queue:
            # 대기 큐에서 가장 소요 시간이 짧은 작업 꺼내기
            job_duration, job_start = heapq.heappop(waiting_queue)
            current_time += job_duration #작업 끝낸 시점 갱신
            total_turnaround_time += current_time - job_start # 반환 시간 계산
        else:
            # 대기 큐가 비어 있으면 다음 작업의 요청 시점으로 건너뜀
            current_time = jobs[job_index][0]
    
    # 반환 시간 평균의 정수 부분 반환
    return total_turnaround_time // num_jobs