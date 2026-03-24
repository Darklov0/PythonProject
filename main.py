from logger import Logger

if __name__ == "__main__":
    logger = Logger("Main")
    logger.info("Application started")
    sum = 0
    for i in range(1, 101):
        sum += i
        logger.debug(f"Sum at iteration {i} is {str(sum)}")

    logger.info(f"sum = {str(sum)}")

    try:
        logger.info("")
        logger.info("      ")
    except Exception as e:
        print(e)

    try:
        logger.log("Supergela", "potatoe")
    except Exception as e:
        print(e)

    logger.info("Application finished")
